# R900DUS

## Descrição

Dados de uso do sistema (deprecada)

---

## Resumo

- Campos: 6
- Chave Primária: 0 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USRNAM | String(255) | Sim | Nome do usuário que executou a ação no sistema |
| ACTION | String(1000) | Sim | Ação executada no sistema |
| ACTPAR | String(2000) | Sim | Parâmetros informados na ação |
| ACTTIM | Number(005,0) | Sim | Hora da ação |
| ACTDATE | Date | Sim | Data da ação |
| SYSMOD | String(255) | Sim | Sistema e módulo que executou a ação no sistema |

---

## Chave Primária

Não possui.

---

## Índices

### R900DUSINDICEACTTIM

**Tipo:** Não unico

Campos:
- ACTTIM

### R900DUSINDICEACTDATEACTTIM

**Tipo:** Não unico

Campos:
- ACTDATE
- ACTTIM

---

## Relacionamentos

Nenhum relacionamento cadastrado.
