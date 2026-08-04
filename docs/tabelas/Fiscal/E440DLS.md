# E440DLS

## Descrição

Compras - Notas Fiscais de Entrada - Entrada, Vencimento, Lote, Série

---

## Resumo

- Campos: 47
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| SeqDls | Number(006,0) | Não | Sequência de movimento de item |
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
| CodEtp | Number(004,0) | Sim | Código da espécie/cultura |
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

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc
- SeqDls

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440DLS_005

**Tabela:** E440IPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |

