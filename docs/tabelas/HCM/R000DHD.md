# R000DHD

## Descrição

Definições do Holerite Digital

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AtiHol | String(001) | Sim | Ativar Holerite Digital |
| HorEnv | String(001) | Sim | Horas Envelope |
| FgtEve | String(001) | Sim | FGTS Evento |
| OutPro | String(001) | Sim | Outros Proventos |
| OutDes | String(001) | Sim | Outros Descontos |
| BanCfg | String(001) | Sim | Indica se a configuração de banco para o integrador da wiipo já foi gerada. |
| BanErr | String(001) | Sim | Ocorreu erro na configuração do banco de dados para o integrador da wiipo. |
| SecWip | String(4096) | Sim | Chave secret gerada pela wiipo e necessária para ativação do banco. |
| TokWip | String(512) | Sim | Token gerado pela Wiipo e necessário para ativação do banco. |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
