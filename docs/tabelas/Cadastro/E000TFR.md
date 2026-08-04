# E000TFR

## Descrição

Tabelas - Integrações - Tabelas de preço de Frete

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodTab | String(004) | Não | Código da tabela de preço frete |
| DatIni | Date | Não | Data início de validade da tabela de preço |
| LocEnt | Number(008,0) | Não | Código da localização para a entrega das mercadorias |
| SeqFlc | Number(004,0) | Sim | Sequência da localização do frete |
| CodSer | String(014) | Sim | Código do serviço da tabela de preço de frete |

---

## Chave Primária

- SeqInt

---

## Índices

### E000TFRIndice01

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodTab
- LocEnt
- SeqFlc
- CodSer
- DatIni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
