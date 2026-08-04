# E055PFT

## Descrição

Tabelas - Tributos - Perfil Tributário

---

## Resumo

- Campos: 17
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPft | Number(004,0) | Não | Código do perfil tributário |
| DesPft | String(050) | Não | Descrição do perfil tributário |
| RecPis | String(001) | Não | Indicativo se o perfil tributário considera a recuperação PIS da transação |
| RecCof | String(001) | Não | Indicativo se o perfil tributário considera a recuperação COFINS da transação |
| TriIcm | String(001) | Não | Indicativo se o perfil tributário considera a tributação do ICMS da transação |
| TriIpi | String(001) | Não | Indicativo se o perfil tributário considera a tributação do IPI da transação |
| TriPis | String(001) | Não | Indicativo se o perfil tributário considera a tributação do PIS da transação |
| TriCof | String(001) | Não | Indicativo se o perfil tributário considera a tributação da COFINS da transação |
| TriIrf | String(001) | Não | Indicativo se o perfil tributário considera a tributação do IRRF da transação |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| SitPft | String(001) | Não | Situação do perfil tributário |

---

## Chave Primária

- CodEmp
- CodPft

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
