import io
import os
import subprocess
import tempfile

import docx
import docxtpl
from django.template import loader
from PIL import Image
from rest_framework import exceptions

from .models import AdmitCardTemplate, Application


def convert_doc_to_pdf(input_file):
    temp_file = tempfile.NamedTemporaryFile(
        suffix='.pdf', delete=False
    )
    command = ['/usr/bin/unoconv', '-f', 'pdf',
               '-o', temp_file.name, input_file]
    subprocess.run(command)
    return temp_file.name


def generate_admit_card(application_id):
    application = Application.objects.get(
        id=application_id, details__serial__isnull=False)
    admit_card_template = AdmitCardTemplate.objects.filter(
        venue=application.venue, is_active=True).first().template
    if not admit_card_template:
        raise exceptions.APIException(
            'Admit card template not found for this venue'
        )
    doc = docxtpl.DocxTemplate(admit_card_template)
    # img_personal = docxtpl.InlineImage(doc, io.BytesIO(
    #     application.details.photo_personal.read()), width=docx.shared.Cm(3.5))
    # img_signature = docxtpl.InlineImage(doc, io.BytesIO(
    #     application.details.photo_signature.read()), width=docx.shared.Cm(3.8), height=docx.shared.Cm(1.5))

    pil_img_personal = Image.open(application.details.photo_personal)
    pil_img_personal = pil_img_personal.convert('RGB')

    io_personal = io.BytesIO()
    pil_img_personal.save(io_personal, format="JPEG")
    img_personal = docxtpl.InlineImage(
        doc, io_personal, width=docx.shared.Cm(3.5))
    pil_img_signature = Image.open(application.details.photo_signature)
    pil_img_signature = pil_img_signature.convert('RGB')
    io_signature = io.BytesIO()
    pil_img_signature.save(io_signature, format='JPEG')
    img_signature = docxtpl.InlineImage(
        doc, io_signature, width=docx.shared.Cm(3.8), height=docx.shared.Cm(1.5))
    context = {
        'NAME': application.name,
        'PHOTO': img_personal,
        "SIGNATURE": img_signature,
        "ROLL": application.details.serial,
    }
    doc.render(context)
    temp_file = tempfile.NamedTemporaryFile(
        suffix='.docx', delete=False
    )
    doc.save(temp_file.name)
    temp_file.close()
    pdf = convert_doc_to_pdf(temp_file.name)
    os.unlink(temp_file.name)
    return pdf
