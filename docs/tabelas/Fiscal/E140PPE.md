# E140PPE

## Descrição

Vendas - Nota Fiscal de Saída - Dados do CTe/MDFe - Produto Perigoso

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqCct | Number(004,0) | Não | Sequência da composição da nota fiscal de saída (MDF-e) |
| SeqPpe | Number(004,0) | Não | Sequência dos registros de produto perigoso |
| CodOnu | String(008) | Sim | Número ONU |
| NomEbq | String(200) | Sim | Nome apropriado para embarque do produto |
| CodCla | String(080) | Sim | Classe ou subclasse/divisão, e risco subsidiário/risco secundário |
| CodEmb | String(012) | Sim | Informação do grupo de embalagem do produto |
| QtdTot | String(040) | Sim | Quantidade total por produto |
| VolTip | String(120) | Sim | Quantidade e tipo de volumes |
| PtoFul | String(012) | Sim | Ponto de fulgor. (CT-e) |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqCct
- SeqPpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140PPE_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

