# E049LST

## Descrição

Tabelas - Listas Dinâmicas

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodLst | Number(006,0) | Não | Código da lista dinâmica |
| DesLst | String(150) | Não | Descrição da lista dinâmica |
| MulLst | String(001) | Não | Indica se o item da lista pode ser associado mais de uma vez a um registro |
| TipLst | String(001) | Não | Indica se a lista é de usuário ou padrão do sistema |
| SitLst | String(001) | Não | Indica a situação na qual se encontra a lista |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Código do usuário responsável pela última atualização do registro |
| DatAtu | Date | Sim | Data da última atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da última atualização do registro |

---

## Chave Primária

- CodLst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
