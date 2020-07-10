# Bulma.css

[Bulma](https://bulma.io/) is a CSS framework used by default in py4web. 
You aren't restricted to Bulma but since it's built in you might want
a brief review of how you can use it with py4web.

Bulma is a set of CSS classes that at first appears to do exactly
the wrong them when you include `bulma.css`: it removes most formatting from
HTML elements. You then apply classes to the HTML elements, even when it seems unnecessary. For example, as shown below, a `<table>` element doesn't look that tabular until you apply the Bulma `table` class to it.

## Example: default Bulma is "unformatted"

Here's the source code for a table generated from data, using Bulma (which has already been included via [laout.html](layout-html.md):

```html
[[extend 'layout.html']]
<h1>Tasks</h1>
<table iclass="table is-full-width">
  <tr><th>Priority</th><th>Title</th><th >Description</th><th>Edit</th></tr>
  [[for q in query:]]
    <tr><td>[[=q.priority]]</td><td>[[=q.title]]</td><td>[[=q.description]]</td><td>[[=A('Edit', _href=URL('edit', q.id))]]</td></tr>
  [[pass]]
</table>
[[=A('New task', _href=URL('new'))]]    
</div>
```
Here's what that table looks like with some sample data, using Bulma's default styling:

![Screen shot of Bulma table with default formatting](assets/img/default-bulma-table.png)

## Things py4web already did for you

The Bulma documentation describes a [starter template](https://bulma.io/documentation/overview/start/) but you can disregad that because the default [layout.html](layout-html.md) already includes what's necessary, such as the stylesheet itself, the ][viewport metatag](https://developer.mozilla.org/en-US/docs/Mozilla/Mobile/Viewport_meta_tag), and other boilerplate, so you can just dive right in and use Bulma's features.



