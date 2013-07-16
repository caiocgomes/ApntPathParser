Path Parser
===========

Parse path routes in a Apontador.com URL to obtain data about the POI

example:

parsing the URL: http://www.apontador.com.br/local/sp/sao_paulo/bares_e_casas_noturnas/6L8NU459/veloso.html should output a json document: 

```json
{type: "POI", uf: "SP", city: "Sao Paulo", category: "Bares e Casas Noturnas", lbs_id: "6L8NU459", name: "Veloso", vanity: "veloso.html"}
```


