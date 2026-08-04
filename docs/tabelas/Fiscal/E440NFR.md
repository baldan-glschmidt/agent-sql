# E440NFR

## Descrição

Compras - Nota referenciada da nota fiscal de entrada

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| SeqNfr | Number(003,0) | Não | Sequencia da nota fiscal referenciada |
| OpeNfr | Number(001,0) | Sim | Operação da nota fiscal referenciada |
| EmiNfr | Number(001,0) | Sim | Emissão da nota fiscal referenciada |
| ChvDoe | String(050) | Sim | Chave do documento eletrônico |
| TipPar | Number(001,0) | Sim | Tipo do Participante da nota fiscal referenciada |
| CodPar | Number(009,0) | Sim | Código do participante emitente |
| CodEdc | String(003) | Sim | Espécie da nota fiscal referenciada |
| CodSel | String(020) | Sim | Série legal da nota fiscal referenciada |
| CodSsl | String(002) | Sim | Subsérie legal da nota fiscal referenciada |
| NumNfr | Number(009,0) | Sim | Número da nota fiscal referenciada |
| DatEmi | Date | Sim | Data da emissão da nota fiscal referenciada |
| CodHas | String(050) | Sim | Hash da Nota Fiscal de Energia |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqNfr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
