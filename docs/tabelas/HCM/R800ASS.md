# R800ASS

## Descrição

Assinalamentos da Integração

---

## Resumo

- Campos: 11
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CriSen | String(001) | Sim | Senha do Usuário é Criptografada |
| FunDec | String(050) | Sim | Função do Banco para Descriptografia da Senha do Usuário |
| NomDBl | String(030) | Sim | Nome do Database Link que Possui a Função de Descriptografia |
| DatExe | Date | Sim | Data da Proxima Execucao |
| HorExe | Number(005,0) | Sim | Hora da Proxima Execucao da Integracao |
| PerExe | Number(001,0) | Sim | Periodicidade da Execucao |
| IntExe | Number(003,0) | Sim | Intervalo de Execucao |
| EndEma | String(030) | Sim | Email do Responsável |
| IniGrp | String(010) | Sim | Nome Inicial do Grupo de Usuários |
| TroSen | String(001) | Sim | Define que o Usuário deverá trocar a senha |
| OrdLot | String(001) | Sim | Define a ordenação do lote no log do integra |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
