# R910PBL

## Descrição

Políticas de bloqueio de usuários (só para consultas)

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPol | Number(010,0) | Não | Código da política. |
| DesPol | String(127) | Não | Descrição da política. |
| Bloque | Number(001,0) | Não | 0=O sistema nunca vai bloquear o usuário. 1=O sistema vai bloquear o usuário quando necessário. |
| MaxTen | Number(003,0) | Sim | Quantidade máxima de tentativas de logon mal-sucedidas. |
| DurCon | Number(005,0) | Sim | Duração (em minutos) da contagem de tentativas mal-sucedidas. |
| DesAut | Number(001,0) | Sim | 0=O sistema nunca vai desbloquear a conta. 1=O sistema vai desbloquear a conta depois de um período de tempo. |
| DurBlo | Number(005,0) | Sim | Duração do bloqueio. Depois deste tempo, o sistema vai desbloquear a conta. |

---

## Chave Primária

- CodPol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
