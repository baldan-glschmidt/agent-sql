# E000UNA

## Descrição

Tabelas - Integrações - Usuários Controle Aprovações

---

## Resumo

- Campos: 6
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
| RotNap | Number(002,0) | Não | Código da rotina de controle de níveis de aprovação |
| CodNap | Number(003,0) | Não | Código do nível de aprovação |
| CodUsu | Number(010,0) | Não | Usuário pertencente ao nível da rotina de controle de aprovação |

---

## Chave Primária

- SeqInt

---

## Índices

### E000UNACN_E000UNA

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- RotNap
- CodNap
- CodUsu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
