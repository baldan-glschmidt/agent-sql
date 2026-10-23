# R158USU

## Descrição

Usuários Vinculados ao Local Físico Controlado

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| TipUsu | Number(001,0) | Não | Tipo de usuário do Gestão de Locais Controlados |
| UsLDAP | String(020) | Não | Nome de usuário do LDAP |
| DlLDAP | String(020) | Sim | Usuário do LDAP responsável pela delegação do local físico |
| TipDel | Number(001,0) | Não | Tipo de delegação de usuário do Gestão de Locais Controlados |

---

## Chave Primária

- VerPlf
- CodPlf
- UsLDAP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
