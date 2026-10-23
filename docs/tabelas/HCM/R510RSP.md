# R510RSP

## Descrição

Currículo Web - Recuperação de Senha - Política

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRSP | Number(003,0) | Não | Código da política de recuperação de senha |
| NomRSP | String(040) | Sim | Nome da política de recuperação de senha |
| PubAlv | Number(001,0) | Sim | Público-alvo |
| ObjRSP | String(500) | Sim | Objetivo da política de recuperação de senha |
| TipRSP | Number(001,0) | Sim | Tipo de apresentação dos campos |
| NumAle | Number(002,0) | Sim | Número de campos aleatórios |
| EmaAlt | String(001) | Sim | Permite informar e-mail alternativo para envio de senha |
| EnvSen | Number(001,0) | Sim | Define a forma de recuperação de senha |
| AltSen | String(001) | Sim | Define se o candidato deve alterar senha no próximo login |
| AceCon | String(001) | Sim | Define se o sistema deve acessar o currículo após alteração de senha |

---

## Chave Primária

- CodRSP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
