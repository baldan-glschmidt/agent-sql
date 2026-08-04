# E000DLS

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Entrada, Vencimento, Lote, Série

---

## Resumo

- Campos: 63
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcFil | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIdeFil | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| CgcFor | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIdeFor | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| SeqDls | Number(006,0) | Não | Sequência de movimento de item |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| CodDep | String(010) | Sim | Código do depósito |
| DatEnt | Date | Sim | Data da entrada do produto no depósito |
| DatVlt | Date | Sim | Data de validade do produto no depósito |
| CodLot | String(050) | Sim | Código do Lote de Fabricação para estocagem |
| NumSep | String(050) | Sim | Número de série do produto |
| QtdEst | Number(014,5) | Sim | Quantidade a ser movimentada do estoque |
| ObsDls | String(250) | Sim | Texto da observação |
| VlrDm1 | Number(014,5) | Sim | Valor Dimensão 1 |
| VlrDm2 | Number(014,5) | Sim | Valor Dimensão 2 |
| VlrDm3 | Number(014,5) | Sim | Valor Dimensão 3 |
| VlrDm4 | Number(014,5) | Sim | Valor Dimensão 4 |
| VlrDm5 | Number(014,5) | Sim | Valor Dimensão 5 |
| VlrDm6 | Number(014,5) | Sim | Valor Dimensão 6 |
| CodSlt | String(010) | Sim | Código do status do lote |
| PerGer | Number(005,2) | Sim | Percentual de germinação |
| PerPur | Number(005,2) | Sim | Percentual de pureza |
| PerUmi | Number(005,2) | Sim | Percentual de umidade |
| DatTes | Date | Sim | Data do teste do produto |
| CodEnd | String(020) | Sim | Código do endereçamento de produto |
| CodSaf | String(010) | Sim | Código da safra |
| CodTrm | String(010) | Sim | Código do tratamento |
| CodBnf | String(010) | Sim | Código do beneficiamento |
| CodCat | String(010) | Sim | Código do categoria do lote |
| DatFab | Date | Sim | Data de fabricação do lote |
| NumEpi | Number(009,0) | Sim | Número da execução de inspeção de qualidade |
| CodPne | Number(004,0) | Sim | Código da peneira |
| CodEtp | Number(004,0) | Sim | Código da espécie do tipo de produto |
| CodCul | Number(004,0) | Sim | Código da cultivar |
| NumTer | String(010) | Sim | Número do termo de conformidade |
| NumAog | String(010) | Sim | Número do atestado de origem genética |
| NumCer | String(010) | Sim | Número do certificado de sementes |
| NumBol | String(010) | Sim | Número do boletim de análise de sementes |
| NumAmo | String(010) | Sim | Número da amostra |
| AmoNum | Number(004,0) | Sim | Número da Amostra |
| IndFab | String(001) | Sim | Indicativo se o lote se trata de lote de fabricante |
| CodFab | String(010) | Sim | Código do fabricante |
| LotFab | String(050) | Sim | Código de lote do fabricante |
| VltFab | Date | Sim | Data de validade do produto do fabricante |
| ProFab | String(021) | Sim | Código do produto no Fabricante |
| CodMar | String(010) | Sim | Código da marca do produto |
| GenA01 | String(080) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - A1 |
| GenA02 | String(080) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - A2 |
| GenA03 | String(080) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - A3 |
| GenA04 | String(080) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - A4 |
| GenA05 | String(080) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - A5 |
| GenA06 | String(080) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - A6 |
| GenN01 | Number(013,2) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - N1 |
| GenN02 | Number(013,2) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - N2 |
| GenN03 | Number(013,2) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - N3 |
| GenN04 | Number(013,2) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - N4 |
| GenN05 | Number(013,2) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - N5 |
| GenN06 | Number(013,2) | Sim | Tratamentos externos ao ERP na distribuição lote e série da nota - N6 |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeIpc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000DLSIndice1

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel
- SeqIpc
- SeqDls

### E000DLSIndice2

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel
- SeqIpc
- SeqDls

### E000DLSIndice3

**Tipo:** Não unico

Campos:
- IdeIpc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
