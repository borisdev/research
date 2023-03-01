# Cheat sheet

## Notes

Source text: [Artifactor Labs on LinkedIn](https://www.linkedin.com/company/artifactorlabs/)

- "build strong relationships across platforms"
- "a suite of engagement and discovery tools engagement and discovery tools"

## High-level product questions

1. After the artist-creator user connects with a MetaMask wallet what would she spend her tokens on in your app?
2. Who is the main customer the artist or the collector?
3. Is the main goal of our current project NFT transaction analytics for the creators of the NFT?
4. What are examples of different platforms that you "build strong relationships
  across"?
5. What are examples of the product's discovery tool?
6. What are examples of the product's engagement tool?


## Defining the problem

The objective of this product feature is to show an NFT artists all her collectors.

This [vercel dashboard](https://mvp-git-boris-demo-artifactor.vercel.app/dashboard) is a report to one NFT artist displaying the collector's of her NFT art works.

I see two potential problems.

1. The user waits too much time to see the report (table).
2. The developer/data scientist expends too much cognitive energy to experiment with new
   analytic features.

The technical reason it takes too much time to render is because the Vendor's DB works on 5 queries
of two types for 17s.

The technical reason the developer/data scientists expends too much cognitive
energy is because the data has not been modeled and transformed in a manner that matches her
mental model.


## query `ArtistTokens` 

- duration: 10s
- description: given an artists public ethereum key get all her created NFT tokens [10s = pagination 4 x 2.5] 

**Request**

```
{
   "query":"query ArtistToken($artistAddressSet: [String!], $artistAddress: String, $after: String, $tokenId: String, $contractAddress: String) {\n  artistTokens(\n    filters: {artistAddressSet: $artistAddressSet, artistAddress: $artistAddress, tokenId: $tokenId, contractAddress: $contractAddress}\n    pagination: {after: $after, limit: 1000}\n  ) {\n    tokenId\n    contractAddress\n    projectName\n    artistAddress\n    platform\n    chain\n    owners {\n      owner\n      tokenId\n      balance\n    }\n    metadata {\n      name\n      description\n      image\n    }\n    _cursor\n  }\n}",
   "variables":{
      "artistAddressSet":[
         "0x7d42611012FDbE366Bf4A0481FC0E1aBf15E245A"
      ],
      "after":""
   },
   "operationName":"ArtistToken"
}
```

**Response**

?


## query `NFTTransfers` 

- duration: 7s
- description: ?
- payload is a list of 4000 tokens

**Request**

```
[
   {
      "query":"query Tx($contractAddress: String!, $tokenIdSet: [String!], $after: String) {\n  nftTransfers(\n    filters: {tokenIdSet: $tokenIdSet, contractAddress: $contractAddress}\n    pagination: {sortKey: \"blockNumber\", sortDirection: Ascending, after: $after, limit: 1000}\n  ) {\n    contractAddress\n    tokenId\n    blockNumber\n    txValueETH\n    to\n    _cursor\n  }\n}",
      "variables":{
         "tokenIdSet":[
            "16001348",
            "16000296",
            "16000396",
            "57000318",
            "10061",
            "11975",
            "10065"
         ],
         "contractAddress":"0xb932a70A57673d89f4acfFBE830E8ed7f75Fb9e0"
      }
   },
   {
      "query":"query Tx($contractAddress: String!, $tokenIdSet: [String!], $after: String) {\n  nftTransfers(\n    filters: {tokenIdSet: $tokenIdSet, contractAddress: $contractAddress}\n    pagination: {sortKey: \"blockNumber\", sortDirection: Ascending, after: $after, limit: 1000}\n  ) {\n    contractAddress\n    tokenId\n    blockNumber\n    txValueETH\n    to\n    _cursor\n  }\n}",
      "variables":{
         "tokenIdSet":[
            "370000275",
            "370000437",
            "370000371",
            "370000008",
            "370000022",
            "370000063",
            "370000016"
         ],
         "contractAddress":"0xa7d8d9ef8D8Ce8992Df33D8b8CF4Aebabd5bD270"
      }
   },
   {
      "query":"query Tx($contractAddress: String!, $tokenIdSet: [String!], $after: String) {\n  nftTransfers(\n    filters: {tokenIdSet: $tokenIdSet, contractAddress: $contractAddress}\n    pagination: {sortKey: \"blockNumber\", sortDirection: Ascending, after: $after, limit: 1000}\n  ) {\n    contractAddress\n    tokenId\n    blockNumber\n    txValueETH\n    to\n    _cursor\n  }\n}",
      "variables":{
         "tokenIdSet":[
            "370000384",
            "370000360",
            "370000222",
            "146000156",
            "208000060",
            "208000095"
         ],
         "contractAddress":"0xa7d8d9ef8D8Ce8992Df33D8b8CF4Aebabd5bD270"
      }
   },
   {
      "query":"query Tx($contractAddress: String!, $tokenIdSet: [String!], $after: String) {\n  nftTransfers(\n    filters: {tokenIdSet: $tokenIdSet, contractAddress: $contractAddress}\n    pagination: {sortKey: \"blockNumber\", sortDirection: Ascending, after: $after, limit: 1000}\n  ) {\n    contractAddress\n    tokenId\n    blockNumber\n    txValueETH\n    to\n    _cursor\n  }\n}",
      "variables":{
         "tokenIdSet":[
            "208000003",
            "208000099",
            "208000070",
            "208000046",
            "11975",
            "10065"
         ],
         "contractAddress":"0xb932a70A57673d89f4acfFBE830E8ed7f75Fb9e0"
      }
   },
   {
      "query":"query Tx($contractAddress: String!, $tokenIdSet: [String!], $after: String) {\n  nftTransfers(\n    filters: {tokenIdSet: $tokenIdSet, contractAddress: $contractAddress}\n    pagination: {sortKey: \"blockNumber\", sortDirection: Ascending, after: $after, limit: 1000}\n  ) {\n    contractAddress\n    tokenId\n    blockNumber\n    txValueETH\n    to\n    _cursor\n  }\n}",
      "variables":{
         "tokenIdSet":[
            "56656387881938462344639196998052317519295174739124894217655342118891176329226",
            "56656387881938462344639196998052317519295174739124894217655342118891176329226",
            "56656387881938462344639196998052317519295174739124894217655342118891176329226",
            "56656387881938462344639196998052317519295174739124894217655342118891176329226",
            "56656387881938462344639196998052317519295174739124894217655342094701920518164",
            "56656387881938462344639196998052317519295174739124894217655342094701920518164",
            "56656387881938462344639196998052317519295174739124894217655342094701920518164",
            "56656387881938462344639196998052317519295174739124894217655342094701920518164"
         ],
         "contractAddress":"0x495f947276749Ce646f68AC8c248420045cb7b5e"
      }
   }
]
```

## Technical questions 

1. Can we break down the meaning of this above query together?
2. What is the response to the above query?
3. Can I get a smaller query to play with? I want to play around with a smaller
   version of the second query. I wonder if you can set me up with the same sort
   of env but with a smaller artists?
4. Does the DB allow you to cache results?
5. How much do you pay for each query result?
6. Is iterating fast to experiment with new features relating to new reports
   critical for the business? If so we can transform the data into a relation DB
   (or non-relational), which might give you a powerful tool to accelerate
   development, ie. More analytic experiments with less cognitive load.
7. Is latency a factor, if so a DB will additionally act like a cache, and allow
   you to filter data using a narrow time filter to www.indexing.co to speed
   things up a lot ie. you just need to query the vendor API for the most recent
   blocks? At the same, maybe having the user wait 10s is not such a big deal,
   and less of an issue or business cost than adding a new DB? 
8. Perhaps you can send the query to www.indexing.co customer service?

## TODOs for me

- [ ] I still have not worked out how to optimize the query or the logic.
- [ ] I still need to make a domain model of the data ie. understand your mental
  model of all the data and relationships and what is the most relevant stuff
