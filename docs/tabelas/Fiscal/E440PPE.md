# E440PPE

## Descrição

Compras - Nota Fiscal de Entrada - Dados do MDFe - Produto Perigoso

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| SeqImd | Number(003,0) | Não | Sequência do item no manifesto |
| SeqPpe | Number(004,0) | Não | Sequência dos registros de produto perigoso |
| CodOnu | String(008) | Sim | Número ONU |
| NomEbq | String(200) | Sim | Nome apropriado para embarque do produto |
| CodCla | String(080) | Sim | Classe ou subclasse/divisão, e risco subsidiário/risco secundário |
| CodEmb | String(012) | Sim | Informação do grupo de embalagem do produto |
| QtdTot | String(040) | Sim | Quantidade total por produto |
| VolTip | String(120) | Sim | Quantidade e tipo de volumes |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfc
- SeqImd
- SeqPpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440PPE_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

