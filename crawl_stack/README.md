# crawl_stack
scrapy crawlers.

## Usage
```
scrapy crawl <crawler> -o <output_file>
```
`<crawler>` can be:
- `stackoverflow`  - high voted Python posts on [Stack Overflow](stackoverflow.com).

Example:

```
scrapy crawl stackoverflow -o data/stackoverflow.jsonlines
```
