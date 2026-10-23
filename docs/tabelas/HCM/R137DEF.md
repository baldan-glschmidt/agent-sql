# R137DEF

## Descrição

Definições sobre integração sistema MAP

---

## Resumo

- Campos: 8
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeInt | Number(015,0) | Sim | Identificação da empresa integradora |
| DomUsu | String(100) | Sim | Domínio  MAP para acesso usuário RH |
| DomCan | String(100) | Sim | Domínio  MAP para candidato efetuar os testes |
| IdeUsu | String(020) | Sim | Identificação para usuário realizar logon |
| IdeSen | String(020) | Sim | Senha para usuário realizar logon |
| SalCre | Number(015,0) | Sim | Saldo dos créditos da empresa |
| SeqTes | Number(007,0) | Sim | Última sequência utilizada na solicitação de teste |
| TmpEsp | Number(005,0) | Sim | Tempo máx.(hh:mm) espera de resposta na integração |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
