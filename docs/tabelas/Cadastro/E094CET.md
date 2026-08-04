# E094CET

## Descrição

Cadastros - Especificações Conformidade  Produto - Componentes

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodEct | String(014) | Não | Código da especificação técnica de conformidade de produto |
| SeqCet | Number(004,0) | Não | Sequência do componente da especificação técnica conformidade de produto |
| VlrCe1 | Number(015,6) | Não | Valor alvo p/ especificação de conformidade |
| VlrCe2 | Number(015,6) | Sim | Valor mínimo p/ especificação de conformidade |
| VlrCe3 | Number(015,6) | Sim | Valor máximo p/ especificação de conformidade |
| DesEct | String(050) | Sim | Descrição da especificação técnica de conformidade de produto |
| ObsEct | String(999) | Sim | Texto da observação da especificação técnica de conformidade de produto |

---

## Chave Primária

- CodEmp
- CodEct
- SeqCet

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E094CET_001

**Tabela:** E094ECT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEct | CodEct |

