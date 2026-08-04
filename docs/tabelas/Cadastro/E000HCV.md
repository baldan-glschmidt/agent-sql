# E000HCV

## Descrição

Integrações - Varejo - Histórico de configuração

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqHis | Number(004,0) | Não | Sequência do histórico de alteração |
| CodUsu | Number(010,0) | Não | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Não | Data da última alteração do registro |
| HorAlt | Number(005,0) | Não | Hora da última alteração do registro |
| DesAlt | String(999) | Não | Descrição da alteração |

---

## Chave Primária

- CodEmp
- CodFil
- SeqHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E000HCV_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

