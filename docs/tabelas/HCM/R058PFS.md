# R058PFS

## Descrição

Perfis de usuário para faixa de monitormento de Sinais do Quadro Sinótico

---

## Resumo

- Campos: 10
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PerId | Number(010,0) | Sim |  |
| CodSin | Number(003,0) | Sim | Sinal de Alarme |
| IniFai | Number(005,0) | Sim | Início da Faixa |
| FimFai | Number(005,0) | Sim | Fim da Faixa |
| DiaSem | Number(001,0) | Sim | Dia Semana |
| OpeUsu | Number(001,0) | Sim | Operação do Usuário |
| EnvCmd | String(001) | Sim | Envia Comando |
| LibAcc | String(001) | Sim | Libera Acesso |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| TipAcc | Number(003,0) | Sim | Tipo do Acesso |

---

## Chave Primária

Não possui.

---

## Índices

### R058PFSIndice1

**Tipo:** Não unico

Campos:
- PerId
- CodSin
- IniFai
- DiaSem
- OpeUsu

---

## Relacionamentos

### IR_R058PFS_000

**Tabela:** R058PUQ

| Origem | Destino |
|--------|---------|
| PerId | PerId |

