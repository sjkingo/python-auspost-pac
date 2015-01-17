# Example

Here is a contrived example of looking up by postcode:

```
>>> from auspost_pac.pac import PAC
>>> from pprint import pprint
>>> p = PAC(YOUR_API_KEY_HERE)
>>> bris = p.locality_search(4000)
>>> pprint(bris)
[<Locality 'BRISBANE CITY'>,
 <Locality 'BRISBANE GPO'>,
 <Locality 'PETRIE TERRACE'>,
 <Locality 'SPRING HILL'>,
 <Locality 'BRISBANE ADELAIDE STREET'>]
>>> bris[0].postcode
4000
>>> bris[0].category
'Delivery Area'
>>> bris[0].state
'QLD'
```
