{{ if .Site.Company.Name }}
{{- $name := .Site.Company.Name -}}
{{ else if .Site.Author.FullName }}
{{- $name := .Site.Author.FullName -}} 
{{ else if .FrontMatter.Theme }}
{{- $name := .FrontMatter.Theme -}}
* [{{ $name }}](/)
{{ end }} 

