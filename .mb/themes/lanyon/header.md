{{- if .Site.Company.Name -}}
{{- $name := .Site.Company.Name -}}
{{ else if .Site.Author.FullName }}
{{- $name := .Site.Author.FullName -}} 
{{ else if .FrontMatter.Theme }}
{{- $name := .FrontMatter.Theme -}}
* [Debut](/)
{{- end }} 
* [White papers](/)
* [Press](/)
* [Sales](/)
* [Developer](/)
* [Compliance](/)
* [Partners](/)
* [Contact](/)
* [Pricing](/)

