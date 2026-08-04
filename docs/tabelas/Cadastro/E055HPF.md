# E055HPF

## Descrição

Cadastros - Histórico de alterações do produto/derivação

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
| IdeHpf | Number(009,0) | Não | Identificador do Registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc.) |
| PerFim | Date | Não | Período Final |
| TipHpf | String(001) | Não | Tipo alteração |
| CodIte | String(060) | Sim | Código fiscal do item |
| DesIte | String(255) | Sim | Descrição fiscal do item |

---

## Chave Primária

- IdeHpf

---

## Índices

### E055HPFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodPro
- CodDer
- PerFim
- TipHpf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
