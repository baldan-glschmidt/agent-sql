# R058SES

## Descrição

Separação Especial de Marcações para Colaboradores

---

## Resumo

- Campos: 22
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor na Separação |
| CodFnc | Number(002,0) | Não | Código da Função na Separação |
| DatIni | Date | Não | Data Inicial da Separação |
| DatFim | Date | Não | Data Final da Separação |
| UsoSep | Number(002,0) | Sim | Uso da Marcação Segundo a Separação |
| DirSep | String(001) | Sim | Direção da Marcação Segundo a Separação |
| SitSep | Number(003,0) | Sim | Situação para Marcações de Justificativas |
| TerSai | String(001) | Sim | Término da Situação de Saída Justificada |
| IniSep | Number(005,0) | Sim | Hora de Início da Faixa da Separação |
| FimSep | Number(005,0) | Sim | Hora Fim da Faixa da Separação |
| CodLot | Number(004,0) | Sim | Código do Lote |
| AbrEmp | String(100) | Sim | Abrangência de Empresa |
| AbrTCl | String(100) | Sim | Abrangência de Tipo de Colaborador |
| AbrTco | String(100) | Sim | Abrangência de Tipo de Contrato |
| AbrTsa | String(100) | Sim | Abrangência de Tipo de Salário |
| AbrVin | String(100) | Sim | Abrangência de Vínculo |
| AbrFil | String(100) | Sim | Abrangência Filial |
| AbrEsc | String(100) | Sim | Abrangência Escala |
| AbrLoc | String(1500) | Sim | Abrangência Local |
| AbrNLo | String(100) | Sim | Abrangência Local |

---

## Chave Primária

- CodDsp
- CodPlt
- CodRlg
- CodFnc
- DatIni
- DatFim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058SES_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

