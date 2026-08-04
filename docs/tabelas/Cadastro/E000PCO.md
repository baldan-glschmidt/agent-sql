# E000PCO

## Descrição

Tabelas - Integrações - Definições de Comissões

---

## Resumo

- Campos: 5
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
| CodPco | Number(004,0) | Não | Código período para o controle de comissionamento |
| CptPco | Date | Não | Mês e ano base do comissionamento |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PCOIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CptPco
- CodPco

---

## Relacionamentos

Nenhum relacionamento cadastrado.
