(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["download"],{"0c18":function(t,e,o){},afdd:function(t,e,o){"use strict";var i=o("8336");e["a"]=i["a"]},eda8:function(t,e,o){"use strict";o.r(e);var i=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("v-container",[o("v-row",{attrs:{justify:"center"}},[o("v-col",{attrs:{cols:"12",md:"8",lg:"5"}},[o("v-alert",{attrs:{dense:"",border:"left",outlined:"",type:"info"}},[t._v(" বিশেষ দ্রষ্টব্য: টেকনিকালি সমস্যার কারণে, আইফোন ব্যবহারকারীদের সাফারি ব্রাউজার ব্যবহার করে প্রবেশপত্র সংরক্ষণে সমস্যার সম্মুখীন হচ্ছেন। উক্ত সমস্যাটি এড়িয়ে চলতে সাফারি ব্রাউজারের পরিবর্তে অন্য সকল বিকল্প ব্রাউজার ব্যবহার করে প্রবেশপত্র ডাউনলোড করার জন্যে অনুরোধ জানানো হচ্ছে। ")])],1)],1),o("v-row",{attrs:{justify:"center"}},[o("v-col",{staticClass:"pa-0",attrs:{cols:"12",md:"8",lg:"5"}},[o("v-card-title",{domProps:{textContent:t._s(t.$t("Download Admit Card"))}}),o("v-divider")],1)],1),o("v-row",{attrs:{justify:"center"}},[o("v-col",{staticClass:"px-0",attrs:{cols:"10",md:"8",lg:"5"}})],1),o("v-row",{staticClass:"mt-7"},[o("v-row",{attrs:{align:"center",justify:"center"}},[o("v-col",{attrs:{cols:"12",md:"5"}},[o("v-card",{staticClass:"text-center pa-4",attrs:{outlined:"",flat:""}},[o("v-text-field",{attrs:{label:t.$t("Application ID")},model:{value:t.application_id,callback:function(e){t.application_id=e},expression:"application_id"}}),o("v-btn",{attrs:{outlined:"",color:"primary",loading:t.loading},on:{click:t.download}},[t._v(" "+t._s(this.$t("Download"))+" ")])],1)],1)],1)],1)],1)},s=[],r={name:"ApplicationDownload",metaInfo(){return{titleTemplate:"%s | Admit Card",meta:[{name:"Download Application",content:"Download your application"}]}},data(){return{loading:!1,application_id:this.$route.query.application_id||""}},methods:{download(){this.loading=!0,this.$axios.get("/application/download/",{params:{application_id:this.application_id},responseType:"arraybuffer"}).then(t=>{const e=window.URL.createObjectURL(new Blob([t.data])),o=document.createElement("a");o.href=e,o.setAttribute("download",`application-${this.application_id}.pdf`),document.body.appendChild(o),o.click()}).finally(()=>{this.loading=!1})}}},a=r,n=o("2877"),l=o("6544"),c=o.n(l),d=(o("caad"),o("0c18"),o("10d2")),h=o("afdd"),p=o("9d26"),u=o("f2e7"),m=o("7560"),v=o("a026"),f=v["a"].extend({name:"transitionable",props:{mode:String,origin:String,transition:String}}),g=o("58df"),_=o("d9bd"),b=Object(g["a"])(d["a"],u["a"],f).extend({name:"v-alert",props:{border:{type:String,validator(t){return["top","right","bottom","left"].includes(t)}},closeLabel:{type:String,default:"$vuetify.close"},coloredBorder:Boolean,dense:Boolean,dismissible:Boolean,closeIcon:{type:String,default:"$cancel"},icon:{default:"",type:[Boolean,String],validator(t){return"string"===typeof t||!1===t}},outlined:Boolean,prominent:Boolean,text:Boolean,type:{type:String,validator(t){return["info","error","success","warning"].includes(t)}},value:{type:Boolean,default:!0}},computed:{__cachedBorder(){if(!this.border)return null;let t={staticClass:"v-alert__border",class:{["v-alert__border--"+this.border]:!0}};return this.coloredBorder&&(t=this.setBackgroundColor(this.computedColor,t),t.class["v-alert__border--has-color"]=!0),this.$createElement("div",t)},__cachedDismissible(){if(!this.dismissible)return null;const t=this.iconColor;return this.$createElement(h["a"],{staticClass:"v-alert__dismissible",props:{color:t,icon:!0,small:!0},attrs:{"aria-label":this.$vuetify.lang.t(this.closeLabel)},on:{click:()=>this.isActive=!1}},[this.$createElement(p["a"],{props:{color:t}},this.closeIcon)])},__cachedIcon(){return this.computedIcon?this.$createElement(p["a"],{staticClass:"v-alert__icon",props:{color:this.iconColor}},this.computedIcon):null},classes(){const t={...d["a"].options.computed.classes.call(this),"v-alert--border":Boolean(this.border),"v-alert--dense":this.dense,"v-alert--outlined":this.outlined,"v-alert--prominent":this.prominent,"v-alert--text":this.text};return this.border&&(t["v-alert--border-"+this.border]=!0),t},computedColor(){return this.color||this.type},computedIcon(){return!1!==this.icon&&("string"===typeof this.icon&&this.icon?this.icon:!!["error","info","success","warning"].includes(this.type)&&"$"+this.type)},hasColoredIcon(){return this.hasText||Boolean(this.border)&&this.coloredBorder},hasText(){return this.text||this.outlined},iconColor(){return this.hasColoredIcon?this.computedColor:void 0},isDark(){return!(!this.type||this.coloredBorder||this.outlined)||m["a"].options.computed.isDark.call(this)}},created(){this.$attrs.hasOwnProperty("outline")&&Object(_["a"])("outline","outlined",this)},methods:{genWrapper(){const t=[this.$slots.prepend||this.__cachedIcon,this.genContent(),this.__cachedBorder,this.$slots.append,this.$scopedSlots.close?this.$scopedSlots.close({toggle:this.toggle}):this.__cachedDismissible],e={staticClass:"v-alert__wrapper"};return this.$createElement("div",e,t)},genContent(){return this.$createElement("div",{staticClass:"v-alert__content"},this.$slots.default)},genAlert(){let t={staticClass:"v-alert",attrs:{role:"alert"},on:this.listeners$,class:this.classes,style:this.styles,directives:[{name:"show",value:this.isActive}]};if(!this.coloredBorder){const e=this.hasText?this.setTextColor:this.setBackgroundColor;t=e(this.computedColor,t)}return this.$createElement("div",t,[this.genWrapper()])},toggle(){this.isActive=!this.isActive}},render(t){const e=this.genAlert();return this.transition?t("transition",{props:{name:this.transition,origin:this.origin,mode:this.mode}},[e]):e}}),C=o("8336"),w=o("b0af"),y=o("99d9"),$=o("62ad"),B=o("a523"),x=o("ce7e"),A=o("0fd9"),D=o("8654"),I=Object(n["a"])(a,i,s,!1,null,null,null);e["default"]=I.exports;c()(I,{VAlert:b,VBtn:C["a"],VCard:w["a"],VCardTitle:y["d"],VCol:$["a"],VContainer:B["a"],VDivider:x["a"],VRow:A["a"],VTextField:D["a"]})}}]);