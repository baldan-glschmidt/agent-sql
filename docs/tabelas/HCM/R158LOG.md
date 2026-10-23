# R158LOG

## Descrição

Log do Gestão de Locais Controlados

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
| UUID | String(032) | Não | Universally Unique Identifier |
| DatLog | Date | Não | Data e Hora da ação que está sendo registrada no log |
| UsLDAP | String(020) | Não | Nome de usuário do LDAP |
| RcLDAP | String(020) | Sim | Nome de usuário do LDAP que recebeu a ação |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| TipAGL | Number(002,0) | Não | Tipo de ação do usuário do Gestão de Locais Controlados |
| IdtPes | String(023) | Sim | Identificador da pessoa envolvida na ação |
| NomPes | String(040) | Sim | Nome da pessoa envolvida na ação |
| DatIni | Date | Sim | Data e hora inicial envolvida na ação |
| DatFim | Date | Sim | Data e hora final envolvida na ação |

---

## Chave Primária

- UUID

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
