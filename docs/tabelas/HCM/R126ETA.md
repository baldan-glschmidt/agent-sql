# R126ETA

## Descrição

Requisições - Etapas

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código Requisição |
| CodEta | Number(003,0) | Não | Código Etapa |
| PerIni | Date | Não | Data de Início |
| PerFim | Date | Sim | Data de Final |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| ObsEtp | String(500) | Sim | Observação da etapa |
| EmpRes | Number(004,0) | Sim | Empresa do Responsável |
| TipRes | Number(001,0) | Sim | Tipo do Colaborador Responsável |
| CadRes | Number(009,0) | Sim | Cadastro do Responsável pela Etapa |
| PtsEta | Number(002,0) | Sim | Pontuação da Etapa |
| NotMin | Number(006,3) | Sim | Nota mínima exigida para considerar a etapa cumprida |
| NotMax | Number(006,3) | Sim | Nota máxima exigida para considerar a etapa cumprida |
| AbrPar | String(050) | Sim | Abrangência de Pareceres Válidos para a Etapa ser considerada |
| AbrSit | String(050) | Sim | Abrangência de Situações Válidas para a Etapa ser considerada |

---

## Chave Primária

- CodRqu
- CodEta
- PerIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126ETA_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

### IR_R126ETA_001

**Tabela:** R114ETA

| Origem | Destino |
|--------|---------|
| CodEta | CodEta |

