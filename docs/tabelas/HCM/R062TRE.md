# R062TRE

## Descrição

Cadastro de Tipo de Reações

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRac | Number(003,0) | Não | Código da Reação |
| DesRac | String(030) | Sim | Descrição da Reação |
| EndEma | String(254) | Sim | Endereço do E-mail do Tipo de Ocorrência |
| TxtEma | String(240) | Sim | Texto do E-mail do Tipo de Ocorrência |
| CodLcm | Number(003,0) | Sim | Código do Lote de Comandos do Acesso |
| EndEnt | Number(003,0) | Sim | Endereço da Entrada no Coletor que será gerado o Alarme |
| IntRea | Number(004,0) | Sim | Intervalo em Minutos para Reação |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| GerLog | String(001) | Sim | Gerar LOG para reações automáticas de acesso |

---

## Chave Primária

- CodRac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
