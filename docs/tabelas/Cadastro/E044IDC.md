# E044IDC

## Descrição

Cadastros - Itens Matriz de Distribuição de Custos

---

## Resumo

- Campos: 20
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumTab | Number(009,0) | Não | Número da Tabela |
| CcuDis | String(009) | Sim | Código do Centro de Custo à Distribuir |
| SeqDis | Number(009,0) | Não | Sequência da Distribuição de Custos |
| CcuRec | String(009) | Sim | Código do Centro de Custo à Receber |
| PerDis | Number(007,4) | Sim | Percentual de Distribuição |
| PerOri | Number(007,4) | Sim | Percentual de Distribuição Original |
| CtaRed | Number(007,0) | Sim | Número Reduzido Conta Contábil |
| FilDst | Number(005,0) | Não | Código da filial |
| SeqPri | Number(009,0) | Não | Sequência de Prioridade de Dist. Custos |
| UsuGer | Number(010,0) | Sim | Identificador do usuário |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Identificador do usuário |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodSaf | String(010) | Sim | Código da safra |
| PerSaf | Number(007,4) | Sim | Percentual de Distribuição da Safra |

---

## Chave Primária

- IdeUni

---

## Índices

### E044ICDIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumTab
- SeqDis

---

## Relacionamentos

Nenhum relacionamento cadastrado.
