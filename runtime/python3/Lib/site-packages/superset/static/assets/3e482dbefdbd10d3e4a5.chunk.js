(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[665],{45578:(e,t,a)=>{var l=a(67206),r=a(45652);e.exports=function(e,t){return e&&e.length?r(e,l(t,2)):[]}},27989:(e,t,a)=>{"use strict";a.d(t,{Z:()=>m});var l=a(67294),r=a(51995),i=a(61988),o=a(35932),n=a(74069),s=a(4715),d=a(34858),c=a(11965);const u=r.iK.div`
  display: block;
  color: ${({theme:e})=>e.colors.grayscale.base};
  font-size: ${({theme:e})=>e.typography.sizes.s-1}px;
`,p=r.iK.div`
  padding-bottom: ${({theme:e})=>2*e.gridUnit}px;
  padding-top: ${({theme:e})=>2*e.gridUnit}px;

  & > div {
    margin: ${({theme:e})=>e.gridUnit}px 0;
  }

  &.extra-container {
    padding-top: 8px;
  }

  .confirm-overwrite {
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }

  .input-container {
    display: flex;
    align-items: center;

    label {
      display: flex;
      margin-right: ${({theme:e})=>2*e.gridUnit}px;
    }

    i {
      margin: 0 ${({theme:e})=>e.gridUnit}px;
    }
  }

  input,
  textarea {
    flex: 1 1 auto;
  }

  textarea {
    height: 160px;
    resize: none;
  }

  input::placeholder,
  textarea::placeholder {
    color: ${({theme:e})=>e.colors.grayscale.light1};
  }

  textarea,
  input[type='text'],
  input[type='number'] {
    padding: ${({theme:e})=>1.5*e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
    border-style: none;
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-radius: ${({theme:e})=>e.gridUnit}px;

    &[name='name'] {
      flex: 0 1 auto;
      width: 40%;
    }

    &[name='sqlalchemy_uri'] {
      margin-right: ${({theme:e})=>3*e.gridUnit}px;
    }
  }
`,m=({resourceName:e,resourceLabel:t,passwordsNeededMessage:a,confirmOverwriteMessage:r,addDangerToast:m,onModelImport:h,show:g,onHide:b,passwordFields:y=[],setPasswordFields:f=(()=>{})})=>{const[v,Z]=(0,l.useState)(!0),[w,_]=(0,l.useState)({}),[x,S]=(0,l.useState)(!1),[C,E]=(0,l.useState)(!1),[T,$]=(0,l.useState)([]),[k,I]=(0,l.useState)(!1),N=()=>{$([]),f([]),_({}),S(!1),E(!1),I(!1)},{state:{alreadyExists:A,passwordsNeeded:H},importResource:F}=(0,d.PW)(e,t,(e=>{N(),m(e)}));(0,l.useEffect)((()=>{f(H),H.length>0&&I(!1)}),[H,f]),(0,l.useEffect)((()=>{S(A.length>0),A.length>0&&I(!1)}),[A,S]);return v&&g&&Z(!1),(0,c.tZ)(n.Z,{name:"model",className:"import-model-modal",disablePrimaryButton:0===T.length||x&&!C||k,onHandledPrimaryAction:()=>{var e;(null==(e=T[0])?void 0:e.originFileObj)instanceof File&&(I(!0),F(T[0].originFileObj,w,C).then((e=>{e&&(N(),h())})))},onHide:()=>{Z(!0),b(),N()},primaryButtonName:x?(0,i.t)("Overwrite"):(0,i.t)("Import"),primaryButtonType:x?"danger":"primary",width:"750px",show:g,title:(0,c.tZ)("h4",null,(0,i.t)("Import %s",t))},(0,c.tZ)(p,null,(0,c.tZ)(s.gq,{name:"modelFile",id:"modelFile",accept:".yaml,.json,.yml,.zip",fileList:T,onChange:e=>{$([{...e.file,status:"done"}])},onRemove:e=>($(T.filter((t=>t.uid!==e.uid))),!1),customRequest:()=>{}},(0,c.tZ)(o.Z,{loading:k},"Select file"))),0===y.length?null:(0,c.tZ)(l.Fragment,null,(0,c.tZ)("h5",null,"Database passwords"),(0,c.tZ)(u,null,a),y.map((e=>(0,c.tZ)(p,{key:`password-for-${e}`},(0,c.tZ)("div",{className:"control-label"},e,(0,c.tZ)("span",{className:"required"},"*")),(0,c.tZ)("input",{name:`password-${e}`,autoComplete:`password-${e}`,type:"password",value:w[e],onChange:t=>_({...w,[e]:t.target.value})}))))),x?(0,c.tZ)(l.Fragment,null,(0,c.tZ)(p,null,(0,c.tZ)("div",{className:"confirm-overwrite"},r),(0,c.tZ)("div",{className:"control-label"},(0,i.t)('Type "%s" to confirm',(0,i.t)("OVERWRITE"))),(0,c.tZ)("input",{id:"overwrite",type:"text",onChange:e=>{var t,a;const l=null!=(t=null==(a=e.currentTarget)?void 0:a.value)?t:"";E(l.toUpperCase()===(0,i.t)("OVERWRITE"))}}))):null)}},13434:(e,t,a)=>{"use strict";a.r(t),a.d(t,{default:()=>P});var l=a(45578),r=a.n(l),i=a(51995),o=a(61988),n=a(11064),s=a(31069),d=a(67294),c=a(15926),u=a.n(c),p=a(30381),m=a.n(p),h=a(91877),g=a(93185),b=a(40768),y=a(34858),f=a(32228),v=a(19259),Z=a(20755),w=a(36674),_=a(98289),x=a(38703),S=a(61337),C=a(14114),E=a(83673),T=a(27989),$=a(58593),k=a(70163),I=a(1510),N=a(1629),A=a(8272),H=a(79789),F=a(85156),D=a(34024),M=a(11965);const z=i.iK.div`
  align-items: center;
  display: flex;

  a {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: 1.2;
  }

  svg {
    margin-right: ${({theme:e})=>e.gridUnit}px;
  }
`,B=(0,o.t)('The passwords for the databases below are needed in order to import them together with the charts. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in export files, and should be added manually after the import if they are needed.'),O=(0,o.t)("You are importing one or more charts that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?");(0,N.Z)();const L=(0,n.Z)(),R=async(e="",t,a)=>{var l;const i=e?{filters:[{col:"table_name",opr:"sw",value:e}]}:{},o=u().encode({columns:["datasource_name","datasource_id"],keys:["none"],order_column:"table_name",order_direction:"asc",page:t,page_size:a,...i}),{json:n={}}=await s.Z.get({endpoint:`/api/v1/dataset/?q=${o}`}),d=null==n||null==(l=n.result)?void 0:l.map((({table_name:e,id:t})=>({label:e,value:t})));return{data:r()(d,"value"),totalCount:null==n?void 0:n.count}},U=i.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.base};
`,P=(0,C.ZP)((function(e){var t,a;const{addDangerToast:l,addSuccessToast:r}=e,{state:{loading:i,resourceCount:n,resourceCollection:c,bulkSelectEnabled:p},setResourceCollection:C,hasPerm:N,fetchData:P,toggleBulkSelect:V,refreshData:q}=(0,y.Yi)("chart",(0,o.t)("chart"),l),j=(0,d.useMemo)((()=>c.map((e=>e.id))),[c]),[W,Y]=(0,y.NE)("chart",j,l),{sliceCurrentlyEditing:K,handleChartUpdated:X,openChartEditModal:G,closeChartEditModal:J}=(0,y.fF)(C,c),[Q,ee]=(0,d.useState)(!1),[te,ae]=(0,d.useState)([]),[le,re]=(0,d.useState)(!1),{userId:ie}=e.user,oe=(0,S.OH)(null==ie?void 0:ie.toString(),null),ne=N("can_write"),se=N("can_write"),de=N("can_write"),ce=N("can_export")&&(0,h.cr)(g.T.VERSIONED_EXPORT),ue=[{id:"changed_on_delta_humanized",desc:!0}],pe=null==F.b||null==(t=F.b.common)||null==(a=t.conf)?void 0:a.ENABLE_BROAD_ACTIVITY_ACCESS,me=e=>{const t=e.map((({id:e})=>e));(0,f.Z)("chart",t,(()=>{re(!1)})),re(!0)},he=e=>null!=e&&e.first_name?`${null==e?void 0:e.first_name} ${null==e?void 0:e.last_name}`:null,ge=(0,d.useMemo)((()=>[...e.user.userId?[{Cell:({row:{original:{id:e}}})=>(0,M.tZ)(w.Z,{itemId:e,saveFaveStar:W,isStarred:Y[e]}),Header:"",id:"id",disableSortBy:!0,size:"sm"}]:[],{Cell:({row:{original:{url:e,slice_name:t,certified_by:a,certification_details:l,description:r}}})=>(0,M.tZ)(z,null,(0,M.tZ)("a",{href:e},a&&(0,M.tZ)(d.Fragment,null,(0,M.tZ)(H.Z,{certifiedBy:a,details:l})," "),t),r&&(0,M.tZ)(A.Z,{tooltip:r,viewBox:"0 -1 24 24"})),Header:(0,o.t)("Chart"),accessor:"slice_name"},{Cell:({row:{original:{viz_type:e}}})=>{var t;return(null==(t=L.get(e))?void 0:t.name)||e},Header:(0,o.t)("Visualization type"),accessor:"viz_type",size:"xxl"},{Cell:({row:{original:{datasource_name_text:e,datasource_url:t}}})=>(0,M.tZ)("a",{href:t},e),Header:(0,o.t)("Dataset"),accessor:"datasource_id",disableSortBy:!0,size:"xl"},{Cell:({row:{original:{last_saved_by:e,changed_by_url:t}}})=>pe?(0,M.tZ)("a",{href:t},he(e)):(0,M.tZ)(d.Fragment,null,he(e)),Header:(0,o.t)("Modified by"),accessor:"last_saved_by.first_name",size:"xl"},{Cell:({row:{original:{last_saved_at:e}}})=>(0,M.tZ)("span",{className:"no-wrap"},e?m().utc(e).fromNow():null),Header:(0,o.t)("Last modified"),accessor:"last_saved_at",size:"xl"},{accessor:"owners",hidden:!0,disableSortBy:!0},{Cell:({row:{original:{created_by:e}}})=>e?`${e.first_name} ${e.last_name}`:"",Header:(0,o.t)("Created by"),accessor:"created_by",disableSortBy:!0,size:"xl"},{Cell:({row:{original:e}})=>se||de||ce?(0,M.tZ)(U,{className:"actions"},de&&(0,M.tZ)(v.Z,{title:(0,o.t)("Please confirm"),description:(0,M.tZ)(d.Fragment,null,(0,o.t)("Are you sure you want to delete")," ",(0,M.tZ)("b",null,e.slice_name),"?"),onConfirm:()=>(0,b.Gm)(e,r,l,q)},(e=>(0,M.tZ)($.u,{id:"delete-action-tooltip",title:(0,o.t)("Delete"),placement:"bottom"},(0,M.tZ)("span",{role:"button",tabIndex:0,className:"action-button",onClick:e},(0,M.tZ)(k.Z.Trash,null))))),ce&&(0,M.tZ)($.u,{id:"export-action-tooltip",title:(0,o.t)("Export"),placement:"bottom"},(0,M.tZ)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>me([e])},(0,M.tZ)(k.Z.Share,null))),se&&(0,M.tZ)($.u,{id:"edit-action-tooltip",title:(0,o.t)("Edit"),placement:"bottom"},(0,M.tZ)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>G(e)},(0,M.tZ)(k.Z.EditAlt,null)))):null,Header:(0,o.t)("Actions"),id:"actions",disableSortBy:!0,hidden:!se&&!de}]),[se,de,ce,...e.user.userId?[Y]:[]]),be=(0,d.useMemo)((()=>({Header:(0,o.t)("Favorite"),id:"id",urlDisplay:"favorite",input:"select",operator:_.p.chartIsFav,unfilteredLabel:(0,o.t)("Any"),selects:[{label:(0,o.t)("Yes"),value:!0},{label:(0,o.t)("No"),value:!1}]})),[]),ye=(0,d.useMemo)((()=>[{Header:(0,o.t)("Owner"),id:"owners",input:"select",operator:_.p.relationManyMany,unfilteredLabel:(0,o.t)("All"),fetchSelects:(0,b.tm)("chart","owners",(0,b.v$)((e=>l((0,o.t)("An error occurred while fetching chart owners values: %s",e)))),e.user),paginate:!0},{Header:(0,o.t)("Created by"),id:"created_by",input:"select",operator:_.p.relationOneMany,unfilteredLabel:(0,o.t)("All"),fetchSelects:(0,b.tm)("chart","created_by",(0,b.v$)((e=>l((0,o.t)("An error occurred while fetching chart created by values: %s",e)))),e.user),paginate:!0},{Header:(0,o.t)("Chart type"),id:"viz_type",input:"select",operator:_.p.equals,unfilteredLabel:(0,o.t)("All"),selects:L.keys().filter((e=>{var t;return(0,I.X3)((null==(t=L.get(e))?void 0:t.behaviors)||[])})).map((e=>{var t;return{label:(null==(t=L.get(e))?void 0:t.name)||e,value:e}})).sort(((e,t)=>e.label&&t.label?e.label>t.label?1:e.label<t.label?-1:0:0))},{Header:(0,o.t)("Dataset"),id:"datasource_id",input:"select",operator:_.p.equals,unfilteredLabel:(0,o.t)("All"),fetchSelects:R,paginate:!0},...e.user.userId?[be]:[],{Header:(0,o.t)("Certified"),id:"id",urlDisplay:"certified",input:"select",operator:_.p.chartIsCertified,unfilteredLabel:(0,o.t)("Any"),selects:[{label:(0,o.t)("Yes"),value:!0},{label:(0,o.t)("No"),value:!1}]},{Header:(0,o.t)("Search"),id:"slice_name",input:"search",operator:_.p.chartAllText}]),[l,be,e.user]),fe=[{desc:!1,id:"slice_name",label:(0,o.t)("Alphabetical"),value:"alphabetical"},{desc:!0,id:"changed_on_delta_humanized",label:(0,o.t)("Recently modified"),value:"recently_modified"},{desc:!1,id:"changed_on_delta_humanized",label:(0,o.t)("Least recently modified"),value:"least_recently_modified"}];function ve(e){return(0,M.tZ)(D.Z,{chart:e,showThumbnails:oe?oe.thumbnails:(0,h.cr)(g.T.THUMBNAILS),hasPerm:N,openChartEditModal:G,bulkSelectEnabled:p,addDangerToast:l,addSuccessToast:r,refreshData:q,loading:i,favoriteStatus:Y[e.id],saveFavoriteStatus:W,handleBulkChartExport:me})}const Ze=[];return(de||ce)&&Ze.push({name:(0,o.t)("Bulk select"),buttonStyle:"secondary","data-test":"bulk-select",onClick:V}),ne&&(Ze.push({name:(0,M.tZ)(d.Fragment,null,(0,M.tZ)("i",{className:"fa fa-plus"})," ",(0,o.t)("Chart")),buttonStyle:"primary",onClick:()=>{window.location.assign("/chart/add")}}),(0,h.cr)(g.T.VERSIONED_EXPORT)&&Ze.push({name:(0,M.tZ)($.u,{id:"import-tooltip",title:(0,o.t)("Import charts"),placement:"bottomRight"},(0,M.tZ)(k.Z.Import,null)),buttonStyle:"link",onClick:()=>{ee(!0)}})),(0,M.tZ)(d.Fragment,null,(0,M.tZ)(Z.Z,{name:(0,o.t)("Charts"),buttons:Ze}),K&&(0,M.tZ)(E.Z,{onHide:J,onSave:X,show:!0,slice:K}),(0,M.tZ)(v.Z,{title:(0,o.t)("Please confirm"),description:(0,o.t)("Are you sure you want to delete the selected charts?"),onConfirm:function(e){s.Z.delete({endpoint:`/api/v1/chart/?q=${u().encode(e.map((({id:e})=>e)))}`}).then((({json:e={}})=>{q(),r(e.message)}),(0,b.v$)((e=>l((0,o.t)("There was an issue deleting the selected charts: %s",e)))))}},(e=>{const t=[];return de&&t.push({key:"delete",name:(0,o.t)("Delete"),type:"danger",onSelect:e}),ce&&t.push({key:"export",name:(0,o.t)("Export"),type:"primary",onSelect:me}),(0,M.tZ)(_.Z,{bulkActions:t,bulkSelectEnabled:p,cardSortSelectOptions:fe,className:"chart-list-view",columns:ge,count:n,data:c,disableBulkSelect:V,fetchData:P,filters:ye,initialSort:ue,loading:i,pageSize:25,renderCard:ve,showThumbnails:oe?oe.thumbnails:(0,h.cr)(g.T.THUMBNAILS),defaultViewMode:(0,h.cr)(g.T.LISTVIEWS_DEFAULT_CARD_VIEW)?"card":"table"})})),(0,M.tZ)(T.Z,{resourceName:"chart",resourceLabel:(0,o.t)("chart"),passwordsNeededMessage:B,confirmOverwriteMessage:O,addDangerToast:l,addSuccessToast:r,onModelImport:()=>{ee(!1),q(),r((0,o.t)("Chart imported"))},show:Q,onHide:()=>{ee(!1)},passwordFields:te,setPasswordFields:ae}),le&&(0,M.tZ)(x.Z,null))}))}}]);