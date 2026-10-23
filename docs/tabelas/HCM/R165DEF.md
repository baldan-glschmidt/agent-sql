# R165DEF

## Descrição

BS - Definições Trajetos

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Codigo da Empresa |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| EveTra | Number(004,0) | Sim | Evento Integração dos Trajetos |
| RgrTra | Number(003,0) | Sim | Código da Regra Especial Trajeto |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R165DEF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

