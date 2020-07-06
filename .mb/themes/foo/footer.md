{{- /*  Automatically name first item in header    
        based on company name, author name name
        if no company was specified, or just 
        the name of the theme if neither of those
        was specified.
        
*/ -}}
{{- if .Site.Company.Name -}}
{{- $name := .Site.Company.Name -}}
## [{{ $name -}}](/)
{{- else if .Site.Author.FullName -}}
{{- $name := .Site.Author.FullName -}}
## [{{ $name -}}](/)
{{- else }}
## [{{.FrontMatter.Theme}}](/)
{{- end }} 

| SECTIONS      | CONNECTIONS   | About Us       | Your rights              |
| ------------- | ------------- | -------------- |:------------------------ |
| [Sitemap](/)  | [Twitter](/)  | [About](/)     | [Privacy and cookies](/) | 
| [Articles](/) | [Instagram](/)| [Credits](/)   | [Terms of use ](/)       |
| [Tutorials](/)| [LinkedIn](/) | [Media](/)     | [About our ads](/)       |
| [Blog](/)     | [YouTube](/)  |                |                          | 
| [Opinion](/)  | [Instagram](/)|                |                          | 
| [Sitemap](/)  | [Twitter](/)  |                |                          | 
|               | [LinkedIn](/) |                |                          | 
|               | [Podcast](/)  |                |                          |
|               | [RSS](/)      |                |                          |

