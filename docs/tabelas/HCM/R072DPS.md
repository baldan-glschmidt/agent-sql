# R072DPS

## Descrição

Definição de Pesquisa

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPsq | Number(003,0) | Não | Código da pesquisa |
| DesPsq | String(030) | Sim | Descrição da Pesquisa |
| IniPsq | Date | Sim | Data Início da Pesquisa |
| FimPsq | Date | Sim | Data Final da Pesquisa |
| TexCom | String(2000) | Sim | Comentário da Pesquisa |
| ResPsq | String(001) | Sim | Direito de resposta Cargos |
| MinEmp | Number(001,0) | Sim | Qtde Mínima de Empresas |
| MinSal | Number(001,0) | Sim | Qtde Mínima de Frequências |
| EmpPmt | Number(008,0) | Sim | Código da Empresa Promotora |
| CodIdm | Number(003,0) | Sim | Índice Reajuste Salários |
| QtdInf | Number(002,0) | Sim | Qtde Cargos Disp.Acima do Inf |
| TipAju | String(001) | Sim | Ajustar por Pontos |
| MerMin | Number(001,0) | Sim | Qtde Mínima Empresas Mercado |
| TipPon | String(001) | Sim | Usat Pontuação |

---

## Chave Primária

- CodPsq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R072DPS_008

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| EmpPmt | CodOem |

### IR_R072DPS_009

**Tabela:** R026IDM

| Origem | Destino |
|--------|---------|
| CodIdm | CodIdm |

