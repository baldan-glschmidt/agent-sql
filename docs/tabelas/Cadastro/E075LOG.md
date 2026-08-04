# E075LOG

## Descrição

Impostos - Impostos Por Produto Agro - Log de alterações

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base de vigência da alíquota do imposto |
| SeqLog | Number(003,0) | Não | Sequência do LOG da alteraçção |
| DatLog | Date | Não | Data da alteração |
| HorLog | Number(005,0) | Não | Hora da alteração |
| UsuLog | Number(010,0) | Não | Usuário responsável pela alteração |
| TexLog | String(999) | Não | Texto com campos e alterações |

---

## Chave Primária

- CodEmp
- CodPro
- CodImp
- DatBas
- SeqLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
