# E720VCO

## Descrição

Ficha - Roteiro - Versões Operações Fabricação

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOpr | String(006) | Não | Código da Operação |
| DatAlt | Date | Não | Data da Alteração Válida p/ Custos |
| CodCre | String(008) | Sim | Código do Centro de Recurso (Máquinas/Pessoas/Terceiros) |
| UtiOpr | String(001) | Não | Operação fornece tempos automaticamente p/ os Roteiros (S=Sim, N=Não) |
| TmpPrp | Number(010,4) | Sim | Tempo Proporcional de fabricação conforme unidade de tempo do C. Recurso |
| TmpFix | Number(010,4) | Sim | Tempo Fixo (espera, preparação) conforme unidade de tempo do C. Recurso |
| TmpFrq | Number(012,3) | Sim | Tempo Frequencial em função da quantidade frequencial |
| QtdFrq | Number(014,5) | Sim | Quantidade Frequencial para dimensionar o tempo frequencial |
| UniCre | String(001) | Não | Unidade de Medida de tempo (M=Minuto, S=Segundo, D=Dia, H=Hora) |
| CodCcu | String(009) | Sim | Código do Centro de Custos |
| DatGer | Date | Sim | Data geração de versão |
| LotTec | Number(010,3) | Sim | Lote Técnico ideal, de fabricação a nível de Operação |
| DtiVal | Date | Sim | Data de Validade inicial p/ utilização desta Operação (Opcional) |
| DtfVal | Date | Sim | Data de Validade final p/ utilização desta Operação (Opcional) |
| SelCus | String(001) | Não | Indica se o item será considerado para a área de custos (importação da ficha técnica) |
| VerOpr | String(015) | Sim | Última versão da operação na qual é incrementada em cada nova alteração |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o registro |

---

## Chave Primária

- CodEmp
- CodOpr
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
