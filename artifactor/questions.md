# Cheat sheet

## Notes

Source text: [Artifactor Labs on LinkedIn](https://www.linkedin.com/company/artifactorlabs/)

- "build strong relationships across platforms"
- "a suite of engagement and discovery tools engagement and discovery tools"

# Questions

- After the user connects with a MetaMask wallet what do people spend their tokens for?
- Who is the main customer the artist or the collector?
- Is the main goal of our current project NFT transaction analytics for the creators of the NFT?
- What are examples of different platforms that you "build strong relationships
  across"?
- What are examples of the product's discovery tool?
- What are examples of the product's engagement tool?




Objective: Get all the collectors of the NFT artist
- get all the NFT tokens of the NFT artist
- for each NFT token and generate a query to pull all of its transactions. 
- Q2: Get all the collectors of each NFT token

This [vercel dashboard](https://mvp-git-boris-demo-artifactor.vercel.app/dashboard) is a report to one NFT artist on who are the collector's of his many NFT works.

Your problem is that to create this report takes too much time? 17s?

Your approach is as follows.


queries 

`ArtistTokens` 

10s - 
given an artists public ethereum key get all her created NFT tokens [10s = pagination 4 x 2.5] 

Request

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
Response



`NFTTransfers` 

7s

payload is a list of 4000 tokens

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
