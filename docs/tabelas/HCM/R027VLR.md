# R027VLR

## Descrição

Valores Gerais p/ Empresa

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| ComVlr | Date | Não | Competência Valores Gerais |
| CodVlr | Number(003,0) | Não | Código do Valor Geral |
| DesVlr | String(040) | Sim | Nome do Valor Geral |
| ValVlr | Number(011,2) | Sim | Valor Geral |

---

## Chave Primária

- NumEmp
- ComVlr
- CodVlr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R027VLR_001

**Tabela:** R027VLG

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| ComVlr | ComVlr |

