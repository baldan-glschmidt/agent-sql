# E000UXP

## Descrição

Tabelas - Integrações - Ligação Usuarios x Produtos

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
| CodUsu | Number(010,0) | Não | Código do usuário |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |

---

## Chave Primária

- SeqInt

---

## Índices

### E000UXPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodUsu
- CodPro
- CodDer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
