# R028LVT

## Descrição

Linhas Vale Transporte

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodLin | Number(005,0) | Não | Código da Linha |
| NomLin | String(040) | Sim | Nome da Linha do Vtr |
| CodOem | Number(008,0) | Sim | Código da Empresa Vtr |
| CodMei | Number(002,0) | Sim | Código do Meio Vtr |
| DesVtr | String(001) | Sim | Tipo de Desconto do Vale Transporte |
| QtdKms | Number(003,0) | Sim | Qtde de Quilometros |
| NumItn | String(015) | Sim | Número do Itinerário |
| CodItn | String(029) | Sim | Itinerário |
| ForVal | Number(002,0) | Sim | Empresa Fornecedora de Vales |

---

## Chave Primária

- CodLin

---

## Índices

### R028LVTIndice2

**Tipo:** Não unico

Campos:
- CodOem

### R028LVTIndice3

**Tipo:** Não unico

Campos:
- CodMei

---

## Relacionamentos

### IR_R028LVT_002

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R028LVT_003

**Tabela:** R028MVT

| Origem | Destino |
|--------|---------|
| CodMei | CodMei |

