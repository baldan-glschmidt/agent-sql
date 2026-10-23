# R014CSI

## Descrição

Contribuição Sindical das Empresas

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DatAlt | Date | Não | Data Alteração das Faixas de Contribuição |
| FaiFat | Number(002,0) | Não | Faixa de Faturamento da Empresa |
| ClaSoc | Number(011,2) | Sim | Classe do Capital Social |
| PerAli | Number(004,2) | Sim | Percentual da Alíquota |
| ParAdi | Number(011,2) | Sim | Parcela a Adicionar |

---

## Chave Primária

- CodSin
- DatAlt
- FaiFat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014CSI_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

