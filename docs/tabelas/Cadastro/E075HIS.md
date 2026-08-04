# E075HIS

## Descrição

Cadastros - Produtos - Históricos

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| SeqHis | Number(004,0) | Não | Sequência numérica do histórico do produto |
| DesHis | String(240) | Não | Histórico do produto - informativos e/ou detalhes técnicos |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |
| CodUsu | Number(010,0) | Não | Usuário responsável pela última alteração do registro |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- SeqHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E075HIS_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

