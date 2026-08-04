# E046GNE

## Descrição

Notas Explicativas - Grupos

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| GruNex | String(030) | Não | Grupo de notas explicativas |
| DesGru | String(250) | Sim | Descrição do grupo de notas explicativas |
| ClaGru | String(025) | Sim | Classificação do grupo |
| MskGru | String(020) | Sim | Máscara do grupo de notas explicativas |
| TxtGru | String(9998) | Sim | Texto de cabeçalho do grupo de notas explicativas |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- GruNex

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E046GNE_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

