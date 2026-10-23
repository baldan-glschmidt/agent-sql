# SAM_CREDENCIAL

## Descrição

Tabela de credenciais do SAMSenior que serão replicadas para a G5

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
| ID_CREDENCIAL | Number(009,0) | Não | Identificador da credencial no SAMSenior |
| DATA_EXPIRACAO | Date | Sim | Data e hora de expiração da credencial |
| TECNOLOGIA | Number(001,0) | Não | Tecnologia da credencial |
| NUMERO | String(013) | Não | Número da credencial |
| ID_PESSOA | String(023) | Não | ID da pessoa do GAS |
| ID_PORTARIA | Number(009,0) | Não | ID da portaria do GAS |
| PAPEL | String(050) | Não | Nome do papel |

---

## Chave Primária

- ID_CREDENCIAL

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
