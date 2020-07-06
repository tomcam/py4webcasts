{{- /*  Automatically name first item in header    
        based on company name, author name name
        if no company was specified, or just 
        the name of the theme if neither of those
        was specified.
        
*/ -}}
{{- if .Site.Company.Name -}}
{{- $name := .Site.Company.Name -}}
* [{{ $name -}}](/)
{{- else if .Site.Author.FullName -}}
{{- $name := .Site.Author.FullName -}}
* [{{ $name -}}](/)
{{- else }}
* [{{.FrontMatter.Theme}}](/)
{{- end }} 
* [Events](/)
* [Subscribe](/)
<script>
url = '/.pub/.indexing/docs.json'; 
function loadJSON(url,callback) {   
    var xobj = new XMLHttpRequest();
    function makeCorsRequest(url) {
    var xhr = createCORSRequest('GET', url)
    if (!xhr) {
      alert('Browser too old? CORS not supported')
      return
    }
    xhr.onload = function() {
      var responseText = xhr.responseText;
      alert('responseText: ' + responseText);
    }
    xhr.onerror = function() {
      alert('Error making CORS request')
      xhr.send()
    }
    xobj.overrideMimeType("application/json");
    xobj.open('GET', url, true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
          }
    };
    xobj.send(null);  
}

 

if (document.readyState === "complete" ||
    (document.readyState !== "loading" && !document.documentElement.doScroll)
) {
  initSearch();
} else {
  document.addEventListener("DOMContentLoaded", initSearch);
}
function initSearch() {
  loadJSON(url, function(response) {
    // Parse JSON string into object
      var actual_JSON = JSON.parse(response);
   });
}
function lsearch(){
alert(document.searchForm.search.value);
return false;}
</script>
<form name="searchForm" onSubmit="lsearch()"><input type="text" id="search" name="search"><span class='icn icn-find'> </span>
</form>


