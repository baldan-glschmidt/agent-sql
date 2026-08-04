# E140CCT

## Descrição

Vendas - Nota Fiscal de Saída - Composição do Conhecimento de Transporte

---

## Resumo

- Campos: 41
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqCct | Number(004,0) | Não | Seqüência da composição do conhecimento de transporte |
| DatEmi | Date | Não | Data de emissão da nota fiscal transportada |
| CodEdc | String(003) | Não | Espécie de documento da nota fiscal transportada para fins fiscais |
| CodSel | String(020) | Não | Código da Série Legal da nota fiscal transportada |
| CodSsl | String(002) | Sim | Código da Subsérie Legal da nota fiscal transportada |
| NumNft | Number(009,0) | Não | Número da nota fiscal transportada |
| VlrTot | Number(015,2) | Não | Valor total da nota fiscal transportada |
| QtdMer | Number(014,5) | Sim | Quantidade das mercadorias da nota fiscal transportada |
| UniMed | String(003) | Sim | Unidade de medida das mercadorias da nota fiscal transportada |
| ChvNel | String(050) | Sim | Chave de acesso da nota fiscal eletrônica |
| VlrMer | Number(015,2) | Sim | Valor das mercadorias constantes no documento fiscal |
| PesBru | Number(014,5) | Sim | Peso bruto da nota fiscal transportada |
| PesLiq | Number(014,5) | Sim | Peso líquido da nota fiscal transportada |
| VlrBic | Number(015,2) | Sim | Valor base do ICMS |
| VlrIcm | Number(015,2) | Sim | Valor do ICMS |
| VlrBsi | Number(015,2) | Sim | Valor base do ICMS Substituído |
| VlrSic | Number(015,2) | Sim | Valor do ICMS Substituído |
| ComNat | String(004) | Sim | Natureza de operação (CFOP) predominante |
| PinSuf | Number(009,0) | Sim | Protocolo de ingresso de mercadoria nacional |
| QtdVol | Number(006,0) | Sim | Quantidade de volumes da nota fiscal de saída |
| EmpNft | Number(004,0) | Sim | Código da empresa da nota fiscal transportada |
| FilNft | Number(005,0) | Sim | Código da filial da nota fiscal transportada |
| SnfNft | String(003) | Sim | Código da série da nota fiscal transportada |
| MedCte | String(002) | Sim | Unidade de medida da quantidade da carga do CTe |
| TipMed | String(020) | Sim | Tipo da unidade de medida da quantidade da carga do CTe |
| QtdMed | Number(013,4) | Sim | Quantidade da unidade de medida da informação da carga do CTe |
| TipDoo | String(002) | Sim | Tipo de documento originário (CT-e) |
| DesTdc | String(100) | Sim | Descrição do tipo de documento (CT-e) |
| NumDoc | String(050) | Sim | Número do documento (CT-e), no caso de informações dos demais documentos |
| TipDoc | String(001) | Sim | Tipo de documento vinculado (Nota Fiscal/Outros Documentos) |
| DatPec | Date | Sim | Data prevista de entrega no cliente |
| NumRom | String(040) | Sim | Número do romaneio da nota fiscal |
| NumPed | String(040) | Sim | Número do pedido da nota fiscal |
| VdiFcs | Number(015,2) | Sim | Somatório do valor diferido do ICMS relativo ao FCP |
| EfiFcs | Number(015,2) | Sim | Somatório do valor efetivo do ICMS relativo ao FCP |
| VicSdt | Number(015,2) | Sim | Somatório do valor do ICMS-ST desonerado |
| SeqMtr | Number(004,0) | Sim | Sequência (ordem) do modal |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqCct

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140CCT_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140CCT_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

