# E140NFR

## Descrição

Vendas - Nota referenciada da nota fiscal de saída

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
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
| FinNfe | Number(001,0) | Sim | Tipo Finalidade da NF-e |
| NfeDeb | Number(002,0) | Sim | Tipo de Nota de Débito |
| NfeCre | Number(002,0) | Sim | Tipo de Nota de Crédito |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqNfr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
