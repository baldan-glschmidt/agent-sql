# E044IGF

## Descrição

Cadastros - Itens Matriz de Gastos por Filial

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial de Origem |
| NumTab | Number(009,0) | Não | Número da Tabela |
| SeqDis | Number(009,0) | Não | Sequência da Distribuição de Cultura |
| FisDes | Number(005,0) | Não | Código da filial de Destino |
| CcuDis | String(009) | Sim | Código do Centro de Custo à Distribuir |
| PerDis | Number(007,4) | Sim | Percentual de Distribuição |
| PerOri | Number(007,4) | Sim | Percentual de Distribuição Original |
| CtaRed | Number(007,0) | Sim | Número Reduzido Conta Contábil |
| CtaRdt | Number(007,0) | Sim | Número Reduzido da Conta Redutora do Grupo |
| CtaRec | Number(007,0) | Sim | Conta Reduzida a Receber |
| CcuRec | String(009) | Sim | Código do Centro de Custo à Receber |
| UsuGer | Number(010,0) | Sim | Identificador do usuário |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Identificador do usuário |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E044IGFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumTab
- SeqDis

---

## Relacionamentos

Nenhum relacionamento cadastrado.
