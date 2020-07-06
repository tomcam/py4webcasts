{{- /*  Automatically name first item in header    
        based on company branding, then name, then
        author name, then theme name, in descending
        order of importance.

{{ if .Site.Company.Name }}
{{- $name := .Site.Company.Name -}}
{{ else if .Site.Author.FullName }}
{{- $name := .Site.Author.FullName -}} 
{{ else if .FrontMatter.Theme }}
{{- $name := .FrontMatter.Theme -}}
* [{{- $name -}}](/)
{{ end }} * [Product](/)



*/ -}}
* [~~chill~~in'](/)
* [Create](/)
* [Pricing](/)
* [Try it Free](/)

