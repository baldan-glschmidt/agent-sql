# R182DEF

## Descrição

PLR - Definições

---

## Resumo

- Campos: 37
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CmpPpr | Date | Não | Competência de Cálculo do PPR |
| DatIni | Date | Sim | Data Início Apuração |
| DatFim | Date | Sim | Data Final Apuração |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código Evento a Integrar |
| CodCal | Number(005,0) | Sim | Código Cálculo a Integrar |
| AdmPer | String(001) | Sim | Admitidos no Período |
| DemSem | String(001) | Sim | Demitidos sem Justa Causa |
| DemCom | String(001) | Sim | Demitidos com Justa Causa |
| DesVol | String(001) | Sim | Desligamento Voluntário |
| SitJus | String(100) | Sim | Situações Absenteísmo Justificado |
| SitInj | String(100) | Sim | Situações Absenteísmo Injustificado |
| SitOci | String(100) | Sim | Situações que Caracterizam Ócio |
| MotOci | String(100) | Sim | Motivos que Caracterizam Ócio |
| IndBas | String(001) | Sim | Indicador Base de Cálculo |
| PerTod | Number(011,2) | Sim | % Todos Colaboradores |
| PerMet | Number(011,2) | Sim | % Atingimento Metas |
| PerAva | Number(011,2) | Sim | % Avaliação de Equipes |
| BasCal | Number(011,2) | Sim | Base de Cálculo |
| TipDiv | String(001) | Sim | Tipo Divisão |
| LocSem | String(001) | Sim | Valor Local sem Direito |
| ColSem | String(001) | Sim | Valor Colaborador sem Direito |
| MinLoc | Number(011,2) | Sim | Pontuação Mínima para o Local |
| MinCol | Number(011,2) | Sim | Pontuação Mínima Colaborador |
| VlrMax | Number(011,2) | Sim | Valor Máximo para o Colaborador |
| VlrMin | Number(011,2) | Sim | Valor Mínimo para o Colaborador |
| AbrCad | String(100) | Sim | Abr.Colaborador |
| AbrFil | String(100) | Sim | Abr.Filial |
| AbrLoc | String(1500) | Sim | Abr.Local |
| AbrSin | String(100) | Sim | Abr.Sindicato |
| AbrTco | String(100) | Sim | Abr.Tipo Contrato |
| AbrTsa | String(100) | Sim | Abr.Tipo Salário |
| AbrSit | String(100) | Sim | Abr.Situação |
| AbrEtb | String(100) | Sim | Abr.Estabilidade |
| AbrVin | String(100) | Sim | Abr.Vínculo |
| AbrCar | String(100) | Sim | Abr.Cargo |

---

## Chave Primária

- NumEmp
- CmpPpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R182DEF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

